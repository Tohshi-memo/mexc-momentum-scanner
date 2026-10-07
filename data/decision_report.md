# Decision Report

- generated_at: 2026-10-07T23:16:27.922042+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16296**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.31% / filled 20/20。**
- 全期間 MARKET基準: n=16296, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +4.51% | **+2.08%** |
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.21% | **+0.66%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.93% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.55% | **+1.10%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.90% | **+0.27%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.44% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 232件 (TP 84 / SL 141 / EXP 7)
- 最新: BEAT/USDT:USDT TP_HIT PnL +3.87% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.43** / 初期 $100.00 (+1222.43%)
- 確定: 6277件 (Win 1845 / Loss 2011 / Flat 2421) / skip 6580件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,322.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6075件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000353 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-07T23:16:16.170864+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=83187.0
- Funnel: target 1073 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MET/USDT:USDT | +37.40% | $8,651,709.59 |
| JUP/USDT:USDT | +13.09% | $13,771,319.49 |
| JTO/USDT:USDT | +8.05% | $3,647,380.39 |
| ACE/USDT:USDT | +7.27% | $1,082,467.12 |
| ORCA/USDT:USDT | +7.23% | $7,556,736.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NGAS/USDT:USDT | below_1h_threshold | +1.31% | +1.32% |
| SYN/USDT:USDT | below_1h_threshold | +1.14% | +1.15% |
| ZEN/USDT:USDT | below_1h_threshold | +0.95% | +0.97% |
| LDO/USDT:USDT | below_1h_threshold | +0.73% | +0.75% |
| BTW/USDT:USDT | below_1h_threshold | +0.52% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
