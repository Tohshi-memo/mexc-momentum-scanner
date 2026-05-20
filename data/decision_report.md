# Decision Report

- generated_at: 2026-05-20T18:53:57.393158+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4568**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4568, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.88% | **-1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.12% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.38% | **+1.35%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.86% | **+1.30%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.84% | **+1.10%** |
| ASK_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.50** / 初期 $100.00 (+24.50%)
- 確定: 530件 (Win 137 / Loss 178 / Flat 215) / skip 599件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $124.50

## 4. Latest Market Context

- 更新: 2026-05-20T18:53:52.178771+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=77380.2
- Funnel: target 759 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +51.79% | $45,341,639.55 |
| EDEN/USDT:USDT | +11.17% | $28,710,932.42 |
| LAB/USDT:USDT | +9.30% | $44,907,343.51 |
| JTO/USDT:USDT | +9.08% | $1,299,924.20 |
| NIL/USDT:USDT | +7.79% | $1,727,793.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +3.99% | +4.19% |
| BEAT/USDT:USDT | below_1h_threshold | +3.82% | +4.02% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.83% | +3.03% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.37% | +2.57% |
| B/USDT:USDT | below_1h_threshold | +1.10% | +1.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
