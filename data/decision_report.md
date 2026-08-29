# Decision Report

- generated_at: 2026-08-29T08:21:12.524013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12914**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.46% / filled 20/20。**
- 全期間 MARKET基準: n=12914, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.27% | **+2.04%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.59% | **+0.95%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.02% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.36% | **-0.05%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.84** / 初期 $100.00 (+616.84%)
- 確定: 4684件 (Win 1417 / Loss 1537 / Flat 1730) / skip 4791件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $716.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.63** / 初期 $100.00 (+56.63%)
- 確定: 2005件 (Win 545 / Loss 484 / Flat 976) / skip 4320件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.32** / 初期 $100.00 (+16.32%)
- 確定: 2010件 (Win 590 / Loss 774 / Flat 646) / pending 1件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000421 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.32

## 6. Latest Market Context

- 更新: 2026-08-29T08:21:03.513506+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=77511.4
- Funnel: target 1023 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +108.42% | $1,462,599.52 |
| HNT/USDT:USDT | +37.78% | $1,854,738.24 |
| BEAT/USDT:USDT | +26.97% | $16,271,085.54 |
| ONG/USDT:USDT | +18.10% | $3,323,978.72 |
| O/USDT:USDT | +15.67% | $1,010,757.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.68% | +2.77% |
| ONG/USDT:USDT | below_1h_threshold | +2.36% | +2.46% |
| AKE/USDT:USDT | below_1h_threshold | +1.70% | +1.80% |
| BEAT/USDT:USDT | below_1h_threshold | +1.47% | +1.57% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.13% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
