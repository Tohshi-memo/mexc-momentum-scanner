# Decision Report

- generated_at: 2026-05-06T09:17:29.728899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3438**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3438, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.23% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.72% | **+1.55%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.72% | **+1.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定: 1件 (Win 0 / Loss 0 / Flat 1) / skip 0件
- 成長率目線: 平均log +0.000000 / 幾何平均 +0.000% per trade / maxDD +0.00%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $100.00

## 4. Latest Market Context

- 更新: 2026-05-06T09:17:26.990314+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81806.9
- Funnel: target 768 → liquid 197 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +51.27% | $10,293,275.50 |
| ZEC/USDT:USDT | +32.93% | $740,726,037.70 |
| STORJ/USDT:USDT | +30.01% | $2,565,211.88 |
| B3/USDT:USDT | +28.67% | $1,459,387.69 |
| FHE/USDT:USDT | +28.27% | $28,604,288.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +3.44% | +3.56% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.80% | +2.92% |
| PYTH/USDT:USDT | below_1h_threshold | +2.34% | +2.46% |
| ICP/USDT:USDT | below_1h_threshold | +1.90% | +2.02% |
| B3/USDT:USDT | below_1h_threshold | +1.71% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
