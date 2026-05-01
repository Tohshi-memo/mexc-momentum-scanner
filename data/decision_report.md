# Decision Report

- generated_at: 2026-05-01T14:06:50.191564+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2807**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2807, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.86% | **+1.48%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.65% | **+1.48%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.17% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T14:06:48.252107+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78599.9
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +105.43% | $21,351,594.01 |
| UB/USDT:USDT | +72.95% | $20,527,500.83 |
| NFP/USDT:USDT | +62.10% | $1,763,531.97 |
| BR/USDT:USDT | +43.46% | $25,959,452.77 |
| ORCA/USDT:USDT | +34.32% | $11,656,709.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NFP/USDT:USDT | below_1h_threshold | +4.84% | +4.95% |
| UB/USDT:USDT | below_1h_threshold | +2.98% | +3.10% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.53% | +1.65% |
| ST/USDT:USDT | below_1h_threshold | +0.67% | +0.79% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.67% | +0.78% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
