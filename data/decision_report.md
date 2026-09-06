# Decision Report

- generated_at: 2026-09-06T13:01:18.482123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13816**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=13816, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.85% | **+1.20%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.13% | **+0.85%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.58% | **+0.79%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.33% | **+3.55%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.37% | **+0.29%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.21% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$843.38** / 初期 $100.00 (+743.38%)
- 確定: 5122件 (Win 1537 / Loss 1677 / Flat 1908) / skip 5255件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $843.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.18** / 初期 $100.00 (+91.18%)
- 確定: 2561件 (Win 716 / Loss 612 / Flat 1233) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0466 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $191.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定: 2427件 (Win 722 / Loss 925 / Flat 780) / pending 3件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000123 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.27

## 6. Latest Market Context

- 更新: 2026-09-06T13:01:08.902234+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=79881.4
- Funnel: target 1054 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +60.96% | $6,312,310.65 |
| ARB/USDT:USDT | +43.69% | $175,747,957.57 |
| FONE/USDT:USDT | +32.98% | $1,026,282.63 |
| FLOCK/USDT:USDT | +29.68% | $2,213,692.27 |
| COTI/USDT:USDT | +20.81% | $1,371,358.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FONE/USDT:USDT | below_1h_threshold | +1.45% | +1.45% |
| FLOCK/USDT:USDT | below_1h_threshold | +0.59% | +0.59% |
| SOXL/USDT:USDT | below_1h_threshold | +0.54% | +0.54% |
| ARB/USDT:USDT | below_1h_threshold | +0.53% | +0.53% |
| RAY/USDT:USDT | below_1h_threshold | +0.48% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
