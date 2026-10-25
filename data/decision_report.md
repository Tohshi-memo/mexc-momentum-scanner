# Decision Report

- generated_at: 2026-10-25T12:41:14.765541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17428**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17428, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.29% | **+0.45%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.92% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.27% | **+1.15%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,559.12** / 初期 $100.00 (+1459.12%)
- 確定: 6681件 (Win 1944 / Loss 2129 / Flat 2608) / skip 7308件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,559.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$317.10** / 初期 $100.00 (+217.10%)
- 確定: 3971件 (Win 1102 / Loss 933 / Flat 1936) / skip 6868件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1782 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $317.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5586件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000562 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T12:41:04.364221+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=80396.8
- Funnel: target 1071 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +64.63% | $9,159,836.26 |
| CAP/USDT:USDT | +27.62% | $1,636,696.50 |
| T/USDT:USDT | +20.01% | $7,659,677.63 |
| SKYAI/USDT:USDT | +17.35% | $1,238,179.13 |
| TAG/USDT:USDT | +15.99% | $2,075,942.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +1.32% | +1.50% |
| CHIP/USDT:USDT | below_1h_threshold | +1.06% | +1.25% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.72% | +0.90% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.67% | +0.85% |
| KORU/USDT:USDT | below_1h_threshold | +0.47% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
