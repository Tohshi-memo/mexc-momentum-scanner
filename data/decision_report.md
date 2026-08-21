# Decision Report

- generated_at: 2026-08-21T19:51:27.099609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12247**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=12247, expectancy=-0.00%
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
| LIMIT_BB3S | 6/16 | 37.5% | +3.40% | **+1.27%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.23% | **+0.92%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.19% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.32% | **+0.79%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.86% | **+0.64%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.71% | **+0.54%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.52** / 初期 $100.00 (+543.52%)
- 確定: 4371件 (Win 1338 / Loss 1435 / Flat 1598) / skip 4437件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $643.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.44** / 初期 $100.00 (+55.44%)
- 確定: 1856件 (Win 513 / Loss 443 / Flat 900) / skip 3802件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0333 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $155.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1899件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T19:51:16.635043+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77120.0
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +160.82% | $1,664,726.01 |
| CATE/USDT:USDT | +38.09% | $11,208,629.38 |
| JIMOTHY/USDT:USDT | +29.88% | $1,383,464.70 |
| COTI/USDT:USDT | +13.52% | $1,802,299.23 |
| LIT/USDT:USDT | +10.33% | $12,207,767.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.30% | +4.29% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.49% | +3.48% |
| ACE/USDT:USDT | below_1h_threshold | +2.12% | +2.11% |
| HEI/USDT:USDT | below_1h_threshold | +2.07% | +2.06% |
| LIT/USDT:USDT | below_1h_threshold | +1.97% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
