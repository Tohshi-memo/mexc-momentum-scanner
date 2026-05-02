# Decision Report

- generated_at: 2026-05-02T10:51:58.765914+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2894**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2894, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.34% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +5.26% | **+3.68%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.49% | **+3.14%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +5.04% | **+2.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.38% | **+2.02%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T10:51:56.802099+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78215.4
- Funnel: target 755 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +194.84% | $111,397,578.57 |
| TAC/USDT:USDT | +34.96% | $1,458,335.33 |
| TAG/USDT:USDT | +19.53% | $4,294,479.16 |
| BIO/USDT:USDT | +19.41% | $1,932,698.18 |
| KNC/USDT:USDT | +16.60% | $1,852,447.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.85% | +4.89% |
| TAG/USDT:USDT | below_1h_threshold | +4.83% | +4.88% |
| BSB/USDT:USDT | below_1h_threshold | +3.51% | +3.56% |
| USTC/USDT:USDT | below_1h_threshold | +3.09% | +3.14% |
| B/USDT:USDT | below_1h_threshold | +2.23% | +2.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
