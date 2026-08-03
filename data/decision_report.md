# Decision Report

- generated_at: 2026-08-03T03:11:18.242940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10183**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10183, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.31% | **-1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_ATR | 10/20 | 50.0% | -0.19% | **-0.09%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.26% | **-0.20%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.37% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.32% | **+1.86%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.46% | **+0.88%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.58% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3676件 (Win 1166 / Loss 1205 / Flat 1305) / skip 3068件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1282件 (Win 359 / Loss 298 / Flat 625) / skip 2312件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.02** / 初期 $100.00 (+12.02%)
- 確定: 970件 (Win 307 / Loss 381 / Flat 282) / pending 5件 / skip 681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.02

## 6. Latest Market Context

- 更新: 2026-08-03T03:11:10.847313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63115.3
- Funnel: target 922 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +39.12% | $34,433,613.89 |
| BICO/USDT:USDT | +36.30% | $5,079,374.65 |
| BLESS/USDT:USDT | +20.68% | $67,674,648.00 |
| TAKE/USDT:USDT | +17.16% | $1,111,858.62 |
| FHE/USDT:USDT | +11.70% | $1,707,292.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000RATS/USDT:USDT | below_1h_threshold | +4.35% | +4.36% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.94% | +2.95% |
| FHE/USDT:USDT | below_1h_threshold | +2.05% | +2.05% |
| GRVT/USDT:USDT | below_1h_threshold | +0.62% | +0.62% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
