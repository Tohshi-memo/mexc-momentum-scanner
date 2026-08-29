# Decision Report

- generated_at: 2026-08-29T09:36:19.709061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12918**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=12918, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.30% | **+1.24%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.35% | **+0.14%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.13% | **+0.09%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.14** / 初期 $100.00 (+606.14%)
- 確定: 4688件 (Win 1417 / Loss 1540 / Flat 1731) / skip 4791件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $706.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.08** / 初期 $100.00 (+56.08%)
- 確定: 2006件 (Win 545 / Loss 485 / Flat 976) / skip 4323件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0155 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.31** / 初期 $100.00 (+16.31%)
- 確定: 2013件 (Win 591 / Loss 776 / Flat 646) / pending 3件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000363 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.31

## 6. Latest Market Context

- 更新: 2026-08-29T09:36:07.875013+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77633.8
- Funnel: target 1023 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1, 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +99.79% | $1,649,730.48 |
| HNT/USDT:USDT | +67.36% | $2,943,525.71 |
| BEAT/USDT:USDT | +22.42% | $19,276,198.68 |
| ONG/USDT:USDT | +19.71% | $3,872,733.55 |
| O/USDT:USDT | +19.05% | $1,127,156.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.12% | +3.08% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.88% | +2.84% |
| TUT/USDT:USDT | below_1h_threshold | +2.74% | +2.71% |
| ACE/USDT:USDT | below_1h_threshold | +2.47% | +2.44% |
| RIVER/USDT:USDT | below_1h_threshold | +2.38% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
