# Decision Report

- generated_at: 2026-06-11T17:55:56.828475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6388**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6388, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.17% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.20% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.47% | **+0.73%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.21% | **+0.60%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.58%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.77% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.43** / 初期 $100.00 (+53.43%)
- 確定: 1305件 (Win 337 / Loss 414 / Flat 554) / skip 1644件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $153.43

## 4. Latest Market Context

- 更新: 2026-06-11T17:55:53.766324+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.44% price=63447.4
- Funnel: target 782 → liquid 159 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1, 4h RSI 75.9 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +28.74% | $11,322,527.10 |
| VELVET/USDT:USDT | +21.25% | $97,734,027.01 |
| SKYAI/USDT:USDT | +11.42% | $10,999,102.87 |
| ZBT/USDT:USDT | +6.97% | $1,166,630.72 |
| HMSTR/USDT:USDT | +6.00% | $4,703,648.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_relative_strength | +6.39% | +4.95% |
| STG/USDT:USDT | below_relative_strength | +5.28% | +3.84% |
| A/USDT:USDT | below_relative_strength | +5.10% | +3.66% |
| NEAR/USDT:USDT | below_1h_threshold | +4.59% | +3.15% |
| OUSTSTOCK/USDT:USDT | below_1h_threshold | +4.40% | +2.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
