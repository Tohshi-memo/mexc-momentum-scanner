# Decision Report

- generated_at: 2026-09-13T06:41:14.792183+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14398**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14398, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_BB3S | 2/9 | 22.2% | +3.31% | **+0.74%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.55% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +3.70% | **+2.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.12% | **+1.37%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.23% | **+1.17%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5528件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$224.61** / 初期 $100.00 (+124.61%)
- 確定: 2916件 (Win 811 / Loss 690 / Flat 1415) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1338 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $224.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.51** / 初期 $100.00 (+27.51%)
- 確定: 2844件 (Win 848 / Loss 1098 / Flat 898) / pending 5件 / skip 3021件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $127.51

## 6. Latest Market Context

- 更新: 2026-09-13T06:41:04.242649+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=77237.3
- Funnel: target 1068 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +242.02% | $84,564,469.48 |
| VTHO/USDT:USDT | +37.78% | $3,660,016.27 |
| POWR/USDT:USDT | +30.11% | $2,118,323.29 |
| ZCAT/USDT:USDT | +27.96% | $1,295,725.11 |
| ILV/USDT:USDT | +22.26% | $1,809,954.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +4.79% | +4.85% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.63% | +3.68% |
| RIVER/USDT:USDT | below_1h_threshold | +1.26% | +1.31% |
| SAGA/USDT:USDT | below_1h_threshold | +1.21% | +1.27% |
| RAY/USDT:USDT | below_1h_threshold | +1.19% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
