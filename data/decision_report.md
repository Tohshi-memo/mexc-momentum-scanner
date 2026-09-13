# Decision Report

- generated_at: 2026-09-13T05:46:24.511353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14394**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14394, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.70% | **+1.48%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.38% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/13 | 53.8% | +4.31% | **+2.32%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.27% | **+0.83%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.02% | **+0.81%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5524件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$224.26** / 初期 $100.00 (+124.26%)
- 確定: 2912件 (Win 809 / Loss 688 / Flat 1415) / skip 4893件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $224.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.52** / 初期 $100.00 (+27.52%)
- 確定: 2841件 (Win 847 / Loss 1096 / Flat 898) / pending 4件 / skip 3021件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $127.52

## 6. Latest Market Context

- 更新: 2026-09-13T05:46:11.998500+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77272.2
- Funnel: target 1068 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +212.02% | $83,604,766.20 |
| VTHO/USDT:USDT | +48.19% | $3,885,526.29 |
| POWR/USDT:USDT | +32.06% | $2,032,107.99 |
| ZCAT/USDT:USDT | +30.49% | $1,271,779.51 |
| ILV/USDT:USDT | +17.91% | $1,609,506.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +4.54% | +4.42% |
| ZCAT/USDT:USDT | below_1h_threshold | +2.25% | +2.13% |
| VET/USDT:USDT | below_1h_threshold | +2.23% | +2.11% |
| KAS/USDT:USDT | below_1h_threshold | +1.03% | +0.91% |
| STX/USDT:USDT | below_1h_threshold | +0.94% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
