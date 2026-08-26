# Decision Report

- generated_at: 2026-08-26T16:11:18.397486+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12732**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=12732, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.47% | **+1.33%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.27% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.76% | **+1.10%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +4.00% | **+1.50%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.74% | **+0.71%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.72% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.49** / 初期 $100.00 (+616.49%)
- 確定: 4629件 (Win 1407 / Loss 1522 / Flat 1700) / skip 4664件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $716.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4142件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0550 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1982件 (Win 580 / Loss 758 / Flat 644) / pending 0件 / skip 2220件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000196 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-26T16:11:09.217733+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=78104.5
- Funnel: target 1023 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +3.60% | $1,316,874.63 |
| CATE/USDT:USDT | +1.85% | $2,019,826.12 |
| UAI/USDT:USDT | +1.76% | $2,658,355.90 |
| EUL/USDT:USDT | +0.99% | $2,933,897.86 |
| BTR/USDT:USDT | +0.97% | $23,689,026.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +3.42% | +3.26% |
| UAI/USDT:USDT | below_1h_threshold | +1.76% | +1.60% |
| CATE/USDT:USDT | below_1h_threshold | +1.62% | +1.46% |
| USOIL/USDT:USDT | below_1h_threshold | +1.04% | +0.88% |
| EUL/USDT:USDT | below_1h_threshold | +1.00% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
