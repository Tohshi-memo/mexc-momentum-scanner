# Decision Report

- generated_at: 2026-07-08T23:44:51.358570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8511**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8511, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.83% | **+0.64%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.75% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.37% | **+0.44%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$103.58** / 初期 $100.00 (+3.58%)
- 確定トレード: 81件 (TP 29 / SL 51 / EXP 1)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.58
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.02** / 初期 $100.00 (+220.02%)
- 確定: 2699件 (Win 852 / Loss 904 / Flat 943) / skip 2373件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $320.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1280件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0591 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T23:44:43.224675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=62228.4
- Funnel: target 851 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +87.14% | $3,785,685.95 |
| LAB/USDT:USDT | +16.46% | $57,286,495.17 |
| CAP/USDT:USDT | +14.42% | $1,262,362.51 |
| OGN/USDT:USDT | +14.23% | $5,017,636.08 |
| ALLO/USDT:USDT | +13.45% | $11,744,289.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.27% | +4.39% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.88% | +4.00% |
| BSB/USDT:USDT | below_1h_threshold | +2.39% | +2.51% |
| NES/USDT:USDT | below_1h_threshold | +2.07% | +2.19% |
| YFI/USDT:USDT | below_1h_threshold | +1.64% | +1.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
