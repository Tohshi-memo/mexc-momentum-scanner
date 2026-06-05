# Decision Report

- generated_at: 2026-06-05T21:01:46.723643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5761**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5761, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.93% | **+1.54%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.44% | **+1.10%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1011件 (Win 239 / Loss 313 / Flat 459) / skip 1311件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T21:01:43.914492+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=61552.9
- Funnel: target 771 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +24.29% | $34,394,734.25 |
| HOME/USDT:USDT | +20.98% | $7,055,257.52 |
| ALLO/USDT:USDT | +18.73% | $6,561,171.92 |
| OPN/USDT:USDT | +11.60% | $31,171,528.69 |
| LIT/USDT:USDT | +11.17% | $4,435,141.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +0.48% | +0.54% |
| ZEST/USDT:USDT | below_1h_threshold | +0.29% | +0.35% |
| ONDO/USDT:USDT | below_1h_threshold | +0.24% | +0.30% |
| GRASS/USDT:USDT | below_1h_threshold | +0.21% | +0.28% |
| MEME/USDT:USDT | below_1h_threshold | +0.09% | +0.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
