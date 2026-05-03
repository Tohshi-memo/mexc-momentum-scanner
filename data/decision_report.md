# Decision Report

- generated_at: 2026-05-03T19:52:08.872804+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3106**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3106, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.73% | **-2.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 18/20 | 90.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +5.66% | **+3.39%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +4.03% | **+3.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.95% | **+2.66%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.95% | **+1.98%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T19:52:04.872708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78754.2
- Funnel: target 755 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +57.97% | $310,144,702.62 |
| SKYAI/USDT:USDT | +21.94% | $26,433,027.94 |
| MERL/USDT:USDT | +13.07% | $1,094,313.67 |
| H/USDT:USDT | +11.61% | $8,531,180.29 |
| PARTI/USDT:USDT | +10.32% | $1,033,117.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.75% | +4.69% |
| BIO/USDT:USDT | below_1h_threshold | +4.41% | +4.35% |
| PARTI/USDT:USDT | below_1h_threshold | +4.28% | +4.22% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.57% | +3.51% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.38% | +3.32% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
