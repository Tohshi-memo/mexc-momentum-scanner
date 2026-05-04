# Decision Report

- generated_at: 2026-05-04T23:12:42.794907+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3273**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=3273, expectancy=-0.16%
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
| LIMIT_BB3S | 3/7 | 42.9% | +2.22% | **+0.95%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.97% | **+0.77%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.36% | **+0.81%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T23:12:37.995997+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=79877.0
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +22.37% | $53,671,883.87 |
| FHE/USDT:USDT | +18.35% | $2,552,842.37 |
| NAORIS/USDT:USDT | +14.35% | $3,316,976.79 |
| TST/USDT:USDT | +12.28% | $23,731,695.56 |
| TONCOIN/USDT:USDT | +11.32% | $36,165,341.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +4.17% | +4.37% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.03% | +1.23% |
| VELO/USDT:USDT | below_1h_threshold | +0.97% | +1.16% |
| IP/USDT:USDT | below_1h_threshold | +0.68% | +0.88% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.50% | +0.69% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
