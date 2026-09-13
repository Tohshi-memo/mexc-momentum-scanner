# Decision Report

- generated_at: 2026-09-13T11:31:18.102365+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14423**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=14423, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.11% | **+1.06%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.90% | **+0.77%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.32% | **+0.66%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.21%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.94%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.99% | **+0.90%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.11% | **+0.78%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.37% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5553件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$226.35** / 初期 $100.00 (+126.35%)
- 確定: 2941件 (Win 818 / Loss 700 / Flat 1423) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1235 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $226.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.16** / 初期 $100.00 (+27.16%)
- 確定: 2854件 (Win 850 / Loss 1103 / Flat 901) / pending 2件 / skip 3042件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000353 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $127.16

## 6. Latest Market Context

- 更新: 2026-09-13T11:31:08.974345+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=76631.1
- Funnel: target 1068 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1, 4h RSI 90.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +222.66% | $98,094,756.20 |
| STEEM/USDT:USDT | +60.49% | $1,951,252.22 |
| ARK/USDT:USDT | +50.32% | $1,561,216.78 |
| VTHO/USDT:USDT | +36.32% | $3,269,903.70 |
| POWR/USDT:USDT | +30.98% | $2,751,027.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +4.32% | +4.33% |
| UP/USDT:USDT | below_1h_threshold | +3.44% | +3.46% |
| THETA/USDT:USDT | below_1h_threshold | +1.73% | +1.75% |
| REZ/USDT:USDT | below_1h_threshold | +1.32% | +1.33% |
| SOXS/USDT:USDT | below_1h_threshold | +1.00% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
