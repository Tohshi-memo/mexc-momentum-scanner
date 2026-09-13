# Decision Report

- generated_at: 2026-09-13T03:56:25.539109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14375**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14375, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 10/20 | 50.0% | +0.37% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.56% | **+0.06%** |
| LIMIT_6PCT | 12/20 | 60.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 9/20 | 45.0% | -0.38% | **-0.17%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.02% | **+0.81%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S_LONG | 4/11 | 36.4% | +2.00% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5506件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$220.57** / 初期 $100.00 (+120.57%)
- 確定: 2893件 (Win 802 / Loss 680 / Flat 1411) / skip 4893件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $220.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.89** / 初期 $100.00 (+26.89%)
- 確定: 2824件 (Win 841 / Loss 1088 / Flat 895) / pending 5件 / skip 3020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000368 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.89

## 6. Latest Market Context

- 更新: 2026-09-13T03:56:13.040490+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77177.2
- Funnel: target 1068 → liquid 128 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 98.8 >= 65=1, 4h RSI 83.2 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +370.69% | $79,063,358.07 |
| ZCAT/USDT:USDT | +45.08% | $1,205,465.85 |
| POWR/USDT:USDT | +42.13% | $1,761,739.30 |
| LONGXIA/USDT:USDT | +22.24% | $9,894,541.16 |
| STORJ/USDT:USDT | +18.30% | $19,081,089.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +3.89% | +4.00% |
| VET/USDT:USDT | below_1h_threshold | +2.69% | +2.80% |
| THETA/USDT:USDT | below_1h_threshold | +2.14% | +2.25% |
| BSV/USDT:USDT | below_1h_threshold | +2.03% | +2.14% |
| KOMA/USDT:USDT | below_1h_threshold | +0.97% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
