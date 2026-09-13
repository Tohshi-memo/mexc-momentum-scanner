# Decision Report

- generated_at: 2026-09-13T05:21:12.646413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14391, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +4.18% | **+1.88%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.96% | **+1.39%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.57% | **+1.28%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.09% | **+0.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/13 | 53.8% | +4.31% | **+2.32%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.06% | **+1.01%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.52% | **+0.38%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.38% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5522件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$223.88** / 初期 $100.00 (+123.88%)
- 確定: 2909件 (Win 808 / Loss 687 / Flat 1414) / skip 4893件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $223.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.41** / 初期 $100.00 (+27.41%)
- 確定: 2838件 (Win 846 / Loss 1095 / Flat 897) / pending 6件 / skip 3020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $127.41

## 6. Latest Market Context

- 更新: 2026-09-13T05:21:02.644621+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=77222.2
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +294.45% | $82,065,885.37 |
| VTHO/USDT:USDT | +68.81% | $3,472,937.05 |
| ZCAT/USDT:USDT | +31.23% | $1,262,658.29 |
| POWR/USDT:USDT | +28.87% | $2,010,060.46 |
| SAGA/USDT:USDT | +23.25% | $1,047,608.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +3.83% | +3.77% |
| ILV/USDT:USDT | below_1h_threshold | +3.19% | +3.13% |
| ZCAT/USDT:USDT | below_1h_threshold | +2.83% | +2.78% |
| UP/USDT:USDT | below_1h_threshold | +2.37% | +2.31% |
| RAY/USDT:USDT | below_1h_threshold | +1.80% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
