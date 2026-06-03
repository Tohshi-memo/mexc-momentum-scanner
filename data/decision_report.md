# Decision Report

- generated_at: 2026-06-03T08:01:00.301353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5530**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5530, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.01% | **+0.76%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.42% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.19% | **+1.20%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.80% | **+0.90%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.02% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.24** / 初期 $100.00 (+30.24%)
- 確定: 984件 (Win 232 / Loss 304 / Flat 448) / skip 1107件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $130.24

## 4. Latest Market Context

- 更新: 2026-06-03T08:00:55.135822+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=67176.9
- Funnel: target 771 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +38.18% | $14,316,640.60 |
| AIA/USDT:USDT | +30.42% | $1,644,029.32 |
| CLO/USDT:USDT | +28.29% | $3,269,495.39 |
| GENIUS/USDT:USDT | +28.01% | $1,843,470.49 |
| ENA/USDT:USDT | +23.62% | $47,988,339.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +0.87% | +0.89% |
| AIA/USDT:USDT | below_1h_threshold | +0.38% | +0.39% |
| BILL/USDT:USDT | below_1h_threshold | +0.35% | +0.36% |
| KAS/USDT:USDT | below_1h_threshold | +0.30% | +0.31% |
| XPL/USDT:USDT | below_1h_threshold | +0.22% | +0.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
