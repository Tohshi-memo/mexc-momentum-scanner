# Decision Report

- generated_at: 2026-05-12T13:53:27.409322+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4126**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4126, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.09% | **-0.04%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.19% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.39% | **+0.70%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.63** / 初期 $100.00 (+15.63%)
- 確定: 262件 (Win 71 / Loss 89 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000554 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $115.63

## 4. Latest Market Context

- 更新: 2026-05-12T13:53:23.308852+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=80655.8
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1, 4h RSI 76.8 >= 65=1, 4h RSI 83.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +88.55% | $24,943,247.35 |
| GIGA/USDT:USDT | +54.62% | $6,980,550.76 |
| USELESS/USDT:USDT | +42.04% | $10,469,472.85 |
| SKYAI/USDT:USDT | +40.51% | $44,144,021.33 |
| GUA/USDT:USDT | +35.19% | $3,666,172.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.50% | +4.73% |
| SOLV/USDT:USDT | below_1h_threshold | +4.41% | +4.65% |
| USELESS/USDT:USDT | below_1h_threshold | +3.43% | +3.67% |
| INJ/USDT:USDT | below_1h_threshold | +3.19% | +3.43% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.11% | +3.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
