# Decision Report

- generated_at: 2026-09-13T12:26:23.323959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14429**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14429, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.53% | **+0.51%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.37% | **+1.58%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.61% | **+1.44%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.75% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5558件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.92** / 初期 $100.00 (+127.92%)
- 確定: 2947件 (Win 820 / Loss 701 / Flat 1426) / skip 4893件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0718 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $227.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.16** / 初期 $100.00 (+27.16%)
- 確定: 2854件 (Win 850 / Loss 1103 / Flat 901) / pending 2件 / skip 3046件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000356 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $127.16

## 6. Latest Market Context

- 更新: 2026-09-13T12:26:12.738210+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=76808.2
- Funnel: target 1068 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +269.37% | $101,041,049.18 |
| STEEM/USDT:USDT | +50.24% | $2,139,698.15 |
| ARK/USDT:USDT | +46.78% | $2,138,870.22 |
| VTHO/USDT:USDT | +28.62% | $3,326,380.80 |
| BTW/USDT:USDT | +28.01% | $4,036,434.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.32% | +4.24% |
| REZ/USDT:USDT | below_1h_threshold | +3.62% | +3.54% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.59% | +1.51% |
| PI/USDT:USDT | below_1h_threshold | +1.09% | +1.01% |
| SOXS/USDT:USDT | below_1h_threshold | +0.84% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
