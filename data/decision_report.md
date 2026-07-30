# Decision Report

- generated_at: 2026-07-30T13:31:37.116980+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9888**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=9888, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.64% | **+0.48%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2929件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2056件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.99** / 初期 $100.00 (+11.99%)
- 確定: 792件 (Win 260 / Loss 309 / Flat 223) / pending 3件 / skip 564件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000665 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $111.99

## 6. Latest Market Context

- 更新: 2026-07-30T13:31:24.522977+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64781.1
- Funnel: target 920 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +55.39% | $2,862,831.38 |
| SNXX/USDT:USDT | +23.26% | $7,250,906.09 |
| ESP/USDT:USDT | +22.98% | $4,827,019.73 |
| CAP/USDT:USDT | +22.84% | $1,713,771.62 |
| ROBO/USDT:USDT | +20.70% | $1,144,404.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.64% | +4.81% |
| SOXL/USDT:USDT | below_1h_threshold | +4.56% | +4.73% |
| KORU/USDT:USDT | below_1h_threshold | +4.53% | +4.70% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +3.42% | +3.60% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.27% | +3.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
