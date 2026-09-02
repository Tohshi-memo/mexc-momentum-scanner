# Decision Report

- generated_at: 2026-09-02T06:11:33.911031+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13311**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13311, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.85% | **+1.02%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.17% | **+0.95%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +6.99% | **+1.75%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.31% | **+1.29%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$824.64** / 初期 $100.00 (+724.64%)
- 確定: 4939件 (Win 1502 / Loss 1625 / Flat 1812) / skip 4933件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $824.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.43** / 初期 $100.00 (+75.43%)
- 確定: 2290件 (Win 637 / Loss 548 / Flat 1105) / skip 4432件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $175.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000359 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T06:11:22.588094+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77644.9
- Funnel: target 1041 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +47.51% | $1,520,860.16 |
| MAGMA/USDT:USDT | +34.95% | $5,676,814.54 |
| CASHCAT/USDT:USDT | +26.82% | $1,459,687.81 |
| BONER/USDT:USDT | +24.45% | $2,627,716.85 |
| UAI/USDT:USDT | +22.28% | $20,835,409.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +3.36% | +3.32% |
| USELESS/USDT:USDT | below_1h_threshold | +1.44% | +1.41% |
| AKE/USDT:USDT | below_1h_threshold | +0.92% | +0.88% |
| CASHCAT/USDT:USDT | below_1h_threshold | +0.89% | +0.85% |
| BTW/USDT:USDT | below_1h_threshold | +0.81% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
