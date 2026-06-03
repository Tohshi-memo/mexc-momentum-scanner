# Decision Report

- generated_at: 2026-06-03T06:45:47.043191+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5527**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5527, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.70% | **+0.45%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.21% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.73** / 初期 $100.00 (+30.73%)
- 確定: 981件 (Win 231 / Loss 302 / Flat 448) / skip 1107件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $130.73

## 4. Latest Market Context

- 更新: 2026-06-03T06:45:37.090180+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=67266.0
- Funnel: target 773 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +34.48% | $2,958,692.22 |
| PORTAL/USDT:USDT | +28.79% | $14,228,735.46 |
| GENIUS/USDT:USDT | +28.19% | $1,782,357.15 |
| LIT/USDT:USDT | +23.09% | $7,775,484.99 |
| APR/USDT:USDT | +20.54% | $1,300,048.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.87% | +2.91% |
| VVV/USDT:USDT | below_1h_threshold | +2.59% | +2.62% |
| ZORA/USDT:USDT | below_1h_threshold | +2.51% | +2.55% |
| LIT/USDT:USDT | below_1h_threshold | +2.29% | +2.32% |
| EPIC/USDT:USDT | below_1h_threshold | +2.07% | +2.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
