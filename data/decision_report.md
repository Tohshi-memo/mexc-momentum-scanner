# Decision Report

- generated_at: 2026-05-04T17:07:13.118784+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3241**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3241, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.90% | **+1.23%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_4PCT | 16/20 | 80.0% | +1.25% | **+1.00%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.74% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T17:07:11.229207+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=80188.5
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +22.04% | $20,638,786.38 |
| BSB/USDT:USDT | +18.74% | $34,459,071.57 |
| FHE/USDT:USDT | +9.66% | $2,691,128.32 |
| TAG/USDT:USDT | +9.43% | $17,851,741.60 |
| B3/USDT:USDT | +5.28% | $1,017,728.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +2.32% | +2.07% |
| BSB/USDT:USDT | below_1h_threshold | +2.16% | +1.90% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.68% | +1.42% |
| 4/USDT:USDT | below_1h_threshold | +1.51% | +1.25% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.43% | +1.17% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
