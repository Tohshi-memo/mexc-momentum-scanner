# Decision Report

- generated_at: 2026-10-07T00:16:20.646404+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16263**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=16263, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_BB3S | 6/15 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.50% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.06% | **-0.03%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.24% | **-0.15%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.58% | **-0.16%** |
| MARKET_LONG | 20/20 | 100.0% | -0.24% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 232件 (TP 84 / SL 141 / EXP 7)
- 最新: BEAT/USDT:USDT TP_HIT PnL +3.87% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.43** / 初期 $100.00 (+1222.43%)
- 確定: 6275件 (Win 1845 / Loss 2011 / Flat 2419) / skip 6549件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,322.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6042件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4421件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000505 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-07T00:16:09.120564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=85535.6
- Funnel: target 1074 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +19.20% | $9,163,080.37 |
| LONGXIA/USDT:USDT | +15.87% | $7,289,692.25 |
| CHIP/USDT:USDT | +4.45% | $2,561,168.89 |
| ETHFI/USDT:USDT | +4.03% | $7,235,140.60 |
| NIGHT/USDT:USDT | +3.31% | $3,382,717.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +1.01% | +0.99% |
| LPT/USDT:USDT | below_1h_threshold | +0.88% | +0.86% |
| ZRO/USDT:USDT | below_1h_threshold | +0.82% | +0.79% |
| RENDER/USDT:USDT | below_1h_threshold | +0.79% | +0.77% |
| BTW/USDT:USDT | below_1h_threshold | +0.77% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
