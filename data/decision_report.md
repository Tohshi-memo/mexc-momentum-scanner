# Decision Report

- generated_at: 2026-08-01T04:41:23.576771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10059**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=10059, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.91% | **+1.02%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.57% | **+0.94%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.04% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.23% | **-0.13%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.51% | **-0.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.55% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$565.53** / 初期 $100.00 (+465.53%)
- 確定: 3611件 (Win 1152 / Loss 1182 / Flat 1277) / skip 3009件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $565.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2191件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.89** / 初期 $100.00 (+11.89%)
- 確定: 875件 (Win 283 / Loss 346 / Flat 246) / pending 5件 / skip 655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.89

## 6. Latest Market Context

- 更新: 2026-08-01T04:41:14.022673+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63024.5
- Funnel: target 921 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +31.95% | $1,246,756.24 |
| KOMA/USDT:USDT | +27.70% | $18,520,332.24 |
| BTW/USDT:USDT | +23.06% | $2,924,814.39 |
| BANK/USDT:USDT | +18.93% | $28,807,679.37 |
| LAB/USDT:USDT | +16.52% | $2,145,536.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +2.78% | +2.70% |
| ORDI/USDT:USDT | below_1h_threshold | +1.85% | +1.77% |
| ZRO/USDT:USDT | below_1h_threshold | +1.83% | +1.75% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.47% | +1.39% |
| PI/USDT:USDT | below_1h_threshold | +1.29% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
