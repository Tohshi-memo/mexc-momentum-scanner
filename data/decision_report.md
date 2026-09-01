# Decision Report

- generated_at: 2026-09-01T23:31:28.762521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13279**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13279, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +3.24% | **+1.46%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.36% | **+2.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.79% | **+1.95%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.00% | **+1.90%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.53% | **+1.76%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.65% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$836.76** / 初期 $100.00 (+736.76%)
- 確定: 4914件 (Win 1498 / Loss 1615 / Flat 1801) / skip 4926件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $836.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.92** / 初期 $100.00 (+75.92%)
- 確定: 2258件 (Win 632 / Loss 542 / Flat 1084) / skip 4432件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1104 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $175.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2661件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000353 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T23:31:15.529183+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=77378.7
- Funnel: target 1036 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +27.50% | $1,302,178.08 |
| MAGMA/USDT:USDT | +24.61% | $3,343,844.58 |
| UAI/USDT:USDT | +23.43% | $14,959,871.48 |
| ACE/USDT:USDT | +13.17% | $8,614,796.54 |
| FILECOIN/USDT:USDT | +8.37% | $20,509,987.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.30% | +3.12% |
| BEAT/USDT:USDT | below_1h_threshold | +1.73% | +1.55% |
| CHIP/USDT:USDT | below_1h_threshold | +1.46% | +1.28% |
| CRV/USDT:USDT | below_1h_threshold | +1.17% | +0.99% |
| BICO/USDT:USDT | below_1h_threshold | +1.14% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
