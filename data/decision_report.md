# Decision Report

- generated_at: 2026-05-04T23:17:23.749069+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3274**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=3274, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.72% | **+1.37%** |
| LIMIT_BB3S | 3/8 | 37.5% | +2.22% | **+0.83%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.49% | **+0.74%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.34% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T23:17:21.488047+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=79872.2
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.6 >= 65=1, 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +22.08% | $53,964,985.31 |
| B3/USDT:USDT | +20.42% | $1,055,106.44 |
| FHE/USDT:USDT | +19.19% | $2,565,862.03 |
| NAORIS/USDT:USDT | +16.12% | $3,421,245.72 |
| TST/USDT:USDT | +12.32% | $23,763,092.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.29% | +2.49% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.22% | +1.42% |
| FHE/USDT:USDT | below_1h_threshold | +1.02% | +1.22% |
| ON/USDT:USDT | below_1h_threshold | +0.95% | +1.15% |
| OL/USDT:USDT | below_1h_threshold | +0.84% | +1.04% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
