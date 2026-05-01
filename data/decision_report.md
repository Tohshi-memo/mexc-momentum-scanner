# Decision Report

- generated_at: 2026-05-01T19:51:57.296976+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2826**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=2826, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.30% | **+1.30%** |
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.73% | **+0.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +0.44% | **+0.13%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.38% | **+0.04%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T19:51:55.266411+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78357.6
- Funnel: target 756 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +15.31% | $1,773,997.57 |
| TAG/USDT:USDT | +11.28% | $2,916,271.83 |
| MAGMA/USDT:USDT | +11.12% | $1,004,115.16 |
| ZEN/USDT:USDT | +8.69% | $6,212,372.41 |
| FIGHT/USDT:USDT | +7.82% | $1,258,264.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +3.86% | +3.90% |
| RAVE/USDT:USDT | below_1h_threshold | +2.37% | +2.42% |
| LUNC/USDT:USDT | below_1h_threshold | +2.36% | +2.40% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.35% | +2.39% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.32% | +2.36% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
