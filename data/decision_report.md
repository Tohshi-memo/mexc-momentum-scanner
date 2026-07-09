# Decision Report

- generated_at: 2026-07-09T00:25:54.524990+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8512**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8512, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_7PCT | 8/20 | 40.0% | +2.60% | **+1.04%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_BB3S | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_ATR_LONG | 4/20 | 20.0% | +1.41% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$103.06** / 初期 $100.00 (+3.06%)
- 確定トレード: 82件 (TP 29 / SL 52 / EXP 1)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.06
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.02** / 初期 $100.00 (+220.02%)
- 確定: 2700件 (Win 852 / Loss 904 / Flat 944) / skip 2373件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $320.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1281件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0591 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-09T00:25:48.132176+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=62117.3
- Funnel: target 851 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +96.00% | $4,371,028.34 |
| OGN/USDT:USDT | +15.69% | $5,967,617.75 |
| CAP/USDT:USDT | +15.11% | $1,422,236.93 |
| ALLO/USDT:USDT | +12.96% | $11,606,701.97 |
| YFI/USDT:USDT | +12.89% | $1,489,625.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.18% | +3.40% |
| CAP/USDT:USDT | below_1h_threshold | +2.17% | +2.40% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.88% | +2.10% |
| SOXL/USDT:USDT | below_1h_threshold | +1.61% | +1.84% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.61% | +1.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
