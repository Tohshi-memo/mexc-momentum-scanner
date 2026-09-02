# Decision Report

- generated_at: 2026-09-02T07:11:14.122179+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13318**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13318, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +5.17% | **+1.55%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.99% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.61% | **+0.73%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.87% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$828.72** / 初期 $100.00 (+728.72%)
- 確定: 4944件 (Win 1503 / Loss 1626 / Flat 1815) / skip 4935件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $828.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.56** / 初期 $100.00 (+75.56%)
- 確定: 2297件 (Win 638 / Loss 549 / Flat 1110) / skip 4432件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0447 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $175.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2698件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000335 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T07:11:04.439233+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77639.0
- Funnel: target 1041 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +49.48% | $1,612,039.40 |
| MAGMA/USDT:USDT | +37.50% | $6,154,030.14 |
| CASHCAT/USDT:USDT | +30.76% | $1,509,481.37 |
| UAI/USDT:USDT | +23.10% | $21,988,979.89 |
| BONER/USDT:USDT | +20.35% | $2,577,926.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +3.89% | +3.81% |
| BONER/USDT:USDT | below_1h_threshold | +3.46% | +3.38% |
| CHIP/USDT:USDT | below_1h_threshold | +3.28% | +3.20% |
| UAI/USDT:USDT | below_1h_threshold | +1.21% | +1.14% |
| PYTH/USDT:USDT | below_1h_threshold | +1.04% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
