# Decision Report

- generated_at: 2026-08-29T07:11:16.929483+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12907**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=12907, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.43% | **+1.22%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.95% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.82% | **-0.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.18% | **-0.17%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.49% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$712.40** / 初期 $100.00 (+612.40%)
- 確定: 4679件 (Win 1415 / Loss 1535 / Flat 1729) / skip 4789件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $712.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4315件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.94** / 初期 $100.00 (+15.94%)
- 確定: 2003件 (Win 587 / Loss 770 / Flat 646) / pending 5件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.94

## 6. Latest Market Context

- 更新: 2026-08-29T07:11:07.854102+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77417.5
- Funnel: target 1023 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +79.27% | $1,254,859.88 |
| HNT/USDT:USDT | +38.71% | $1,418,163.26 |
| BEAT/USDT:USDT | +19.47% | $13,634,371.09 |
| SKR/USDT:USDT | +16.37% | $1,557,509.66 |
| AKE/USDT:USDT | +14.50% | $20,159,693.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.83% | +3.86% |
| HNT/USDT:USDT | below_1h_threshold | +2.15% | +2.17% |
| TURBO/USDT:USDT | below_1h_threshold | +1.28% | +1.31% |
| DOS/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |
| ONG/USDT:USDT | below_1h_threshold | +0.72% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
