# Decision Report

- generated_at: 2026-08-15T02:01:19.741128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11625**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.56% / filled 20/20。**
- 全期間 MARKET基準: n=11625, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.93% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.10% | **+0.07%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.10% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.78** / 初期 $100.00 (+541.78%)
- 確定: 4093件 (Win 1283 / Loss 1348 / Flat 1462) / skip 4093件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account -0.10% 残高後 $641.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.39** / 初期 $100.00 (+52.39%)
- 確定: 1688件 (Win 482 / Loss 409 / Flat 797) / skip 3348件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0709 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account -0.08% 残高後 $152.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.52** / 初期 $100.00 (+17.52%)
- 確定: 1572件 (Win 478 / Loss 602 / Flat 492) / pending 2件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000164 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.52

## 6. Latest Market Context

- 更新: 2026-08-15T02:01:11.441789+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63014.8
- Funnel: target 985 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIO/USDT:USDT | +22.51% | $1,190,122.64 |
| ROBO/USDT:USDT | +21.14% | $1,309,337.70 |
| US/USDT:USDT | +15.05% | $6,654,025.84 |
| CAP/USDT:USDT | +14.50% | $21,603,964.03 |
| ONE/USDT:USDT | +12.26% | $1,491,165.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +1.56% | +1.55% |
| LINK/USDT:USDT | below_1h_threshold | +0.40% | +0.39% |
| VELVET/USDT:USDT | below_1h_threshold | +0.24% | +0.24% |
| AIO/USDT:USDT | below_1h_threshold | +0.21% | +0.20% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.20% | +0.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
