# Decision Report

- generated_at: 2026-05-14T14:44:23.777121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4299**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4299, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.39% | **+0.77%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.86% | **+0.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.86% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.61** / 初期 $100.00 (+19.61%)
- 確定: 354件 (Win 95 / Loss 127 / Flat 132) / skip 506件
- 成長率目線: 平均log +0.000506 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $119.61

## 4. Latest Market Context

- 更新: 2026-05-14T14:44:20.243508+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.78% price=80289.1
- Funnel: target 763 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=4, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +65.52% | $11,613,443.73 |
| UP/USDT:USDT | +28.78% | $1,791,748.36 |
| PLAY/USDT:USDT | +27.90% | $3,259,346.75 |
| TROLLSOL/USDT:USDT | +27.14% | $2,279,298.32 |
| ESPORTS/USDT:USDT | +23.28% | $1,320,873.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_relative_strength | +5.46% | +4.68% |
| PLAY/USDT:USDT | below_relative_strength | +5.43% | +4.65% |
| CFX/USDT:USDT | below_relative_strength | +5.26% | +4.48% |
| ASTSSTOCK/USDT:USDT | below_relative_strength | +5.10% | +4.31% |
| ZEC/USDT:USDT | below_1h_threshold | +4.84% | +4.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
