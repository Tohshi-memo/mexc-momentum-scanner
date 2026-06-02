# Decision Report

- generated_at: 2026-06-02T11:05:29.721032+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5445**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5445, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_BB3S | 4/14 | 28.6% | +0.64% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.50% | **-0.08%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.14% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 86件 (TP 25 / SL 58 / EXP 3)
- 最新: LIT/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.97** / 初期 $100.00 (+31.97%)
- 確定: 957件 (Win 224 / Loss 290 / Flat 443) / skip 1049件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.97

## 4. Latest Market Context

- 更新: 2026-06-02T11:05:27.058006+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=69559.5
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +43.33% | $3,044,315.60 |
| EPIC/USDT:USDT | +32.54% | $2,424,010.09 |
| MRVLSTOCK/USDT:USDT | +25.94% | $5,605,740.15 |
| ESPORTS/USDT:USDT | +25.71% | $12,823,367.16 |
| LAB/USDT:USDT | +23.40% | $181,462,544.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +2.77% | +2.86% |
| MYX/USDT:USDT | below_1h_threshold | +1.65% | +1.73% |
| OPG/USDT:USDT | below_1h_threshold | +1.32% | +1.41% |
| NEAR/USDT:USDT | below_1h_threshold | +0.75% | +0.83% |
| GRASS/USDT:USDT | below_1h_threshold | +0.72% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
