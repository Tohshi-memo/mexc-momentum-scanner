# Decision Report

- generated_at: 2026-05-01T23:47:05.637895+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2844**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2844, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.49% | **+0.60%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.41% | **+1.57%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.50% | **+1.37%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.89% | **+1.30%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.58% | **+1.08%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.34% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T23:47:03.478408+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78100.0
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1, 4h RSI 91.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +66.71% | $15,906,236.89 |
| CHILLGUY/USDT:USDT | +14.33% | $1,141,109.75 |
| B/USDT:USDT | +11.42% | $61,584,829.61 |
| WOJAK/USDT:USDT | +9.67% | $1,076,927.55 |
| FIGHT/USDT:USDT | +9.56% | $1,267,986.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +3.90% | +3.91% |
| TAG/USDT:USDT | below_1h_threshold | +3.06% | +3.07% |
| PHAROS/USDT:USDT | below_1h_threshold | +2.72% | +2.73% |
| APE/USDT:USDT | below_1h_threshold | +2.64% | +2.65% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +1.62% | +1.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
