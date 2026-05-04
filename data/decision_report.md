# Decision Report

- generated_at: 2026-05-04T05:16:56.360222+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3156**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=3156, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/12 | 41.7% | +1.78% | **+0.74%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.88% | **+0.56%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.98% | **+0.79%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.84% | **+0.74%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T05:16:54.551116+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=80060.9
- Funnel: target 758 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +54.42% | $21,786,050.69 |
| SKYAI/USDT:USDT | +51.97% | $45,423,388.60 |
| LAB/USDT:USDT | +46.55% | $216,216,403.30 |
| TAG/USDT:USDT | +41.97% | $7,213,678.70 |
| TST/USDT:USDT | +41.83% | $6,385,138.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.95% | +4.25% |
| TST/USDT:USDT | below_1h_threshold | +3.91% | +4.21% |
| GONGJIAN/USDT:USDT | below_1h_threshold | +2.81% | +3.11% |
| SAPIEN/USDT:USDT | below_1h_threshold | +2.52% | +2.81% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.94% | +2.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
