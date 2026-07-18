# Decision Report

- generated_at: 2026-07-18T11:16:10.188252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8939**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8939, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.01% | **+0.56%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.28% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.91% | **+1.15%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2451件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.73** / 初期 $100.00 (+11.73%)
- 確定: 900件 (Win 216 / Loss 181 / Flat 503) / skip 1450件
- 成長率目線: 平均log +0.000123 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0743 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.90** / 初期 $100.00 (-1.10%)
- 確定: 192件 (Win 60 / Loss 105 / Flat 27) / pending 4件 / skip 218件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000247 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.90

## 6. Latest Market Context

- 更新: 2026-07-18T11:16:03.753989+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63990.1
- Funnel: target 885 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +50.57% | $71,238,386.46 |
| B/USDT:USDT | +48.26% | $6,700,730.64 |
| TRADOOR/USDT:USDT | +31.39% | $4,687,894.66 |
| XEC/USDT:USDT | +20.91% | $3,498,483.25 |
| ALLO/USDT:USDT | +12.51% | $4,839,185.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.93% | +3.92% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.21% | +3.20% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.91% | +2.90% |
| US/USDT:USDT | below_1h_threshold | +2.42% | +2.41% |
| BASED/USDT:USDT | below_1h_threshold | +1.43% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
