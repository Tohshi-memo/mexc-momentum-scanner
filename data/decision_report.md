# Decision Report

- generated_at: 2026-08-29T09:16:17.059031+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12916**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=12916, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.99% | **+1.89%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.59% | **+0.95%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 4/16 | 25.0% | +2.46% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.11% | **-0.05%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.76% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$709.69** / 初期 $100.00 (+609.69%)
- 確定: 4686件 (Win 1417 / Loss 1539 / Flat 1730) / skip 4791件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $709.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.08** / 初期 $100.00 (+56.08%)
- 確定: 2006件 (Win 545 / Loss 485 / Flat 976) / skip 4321件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0122 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.52** / 初期 $100.00 (+16.52%)
- 確定: 2012件 (Win 591 / Loss 775 / Flat 646) / pending 0件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000428 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.52

## 6. Latest Market Context

- 更新: 2026-08-29T09:16:07.794800+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77621.5
- Funnel: target 1023 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +102.60% | $1,613,666.79 |
| HNT/USDT:USDT | +42.79% | $2,374,908.86 |
| BEAT/USDT:USDT | +27.37% | $18,028,969.50 |
| ONG/USDT:USDT | +22.98% | $3,709,176.27 |
| O/USDT:USDT | +17.36% | $1,100,350.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +3.95% | +3.93% |
| COTI/USDT:USDT | below_1h_threshold | +3.68% | +3.66% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.18% | +3.16% |
| BTR/USDT:USDT | below_1h_threshold | +2.97% | +2.95% |
| TOAD/USDT:USDT | below_1h_threshold | +1.97% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
