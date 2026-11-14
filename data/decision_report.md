# Decision Report

- generated_at: 2026-11-14T09:26:18.515828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18886**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.66% / filled 20/20。**
- 全期間 MARKET基準: n=18886, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.49% | **+1.42%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.52% | **+1.22%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.89% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.69% | **+0.41%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.23% | **+0.15%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7291件 (Win 2100 / Loss 2337 / Flat 2854) / skip 8156件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$415.46** / 初期 $100.00 (+315.46%)
- 確定: 4894件 (Win 1310 / Loss 1079 / Flat 2505) / skip 7403件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0764 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $415.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7044件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T09:26:01.646708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=67022.6
- Funnel: target 1071 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +49.20% | $4,497,266.19 |
| DODO/USDT:USDT | +14.69% | $1,441,560.84 |
| AKE/USDT:USDT | +12.49% | $80,921,645.20 |
| ARIA/USDT:USDT | +4.62% | $4,322,781.41 |
| NIGHT/USDT:USDT | +4.40% | $1,367,844.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +0.37% | +0.29% |
| TESLA/USDT:USDT | below_1h_threshold | +0.18% | +0.10% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.12% | +0.04% |
| XPT/USDT:USDT | below_1h_threshold | +0.08% | -0.00% |
| METASTOCK/USDT:USDT | below_1h_threshold | +0.07% | -0.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
