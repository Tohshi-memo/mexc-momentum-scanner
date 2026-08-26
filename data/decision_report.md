# Decision Report

- generated_at: 2026-08-26T03:01:19.973641+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12649**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.84% / filled 20/20。**
- 全期間 MARKET基準: n=12649, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.28% | **+1.09%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.87% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.91% | **+0.77%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.36% | **+0.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.16% | **+0.15%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.08% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4585件 (Win 1392 / Loss 1506 / Flat 1687) / skip 4625件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1978件 (Win 536 / Loss 473 / Flat 969) / skip 4082件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0678 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.86** / 初期 $100.00 (+13.86%)
- 確定: 1934件 (Win 564 / Loss 740 / Flat 630) / pending 0件 / skip 2184件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $113.86

## 6. Latest Market Context

- 更新: 2026-08-26T03:01:11.239360+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=79081.2
- Funnel: target 1023 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +68.60% | $9,427,969.72 |
| LONGXIA/USDT:USDT | +24.61% | $1,901,460.43 |
| FARTCOIN/USDT:USDT | +12.59% | $15,289,309.74 |
| PONS/USDT:USDT | +9.09% | $1,063,691.12 |
| STX/USDT:USDT | +8.62% | $11,278,688.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +3.68% | +3.66% |
| BMT/USDT:USDT | below_1h_threshold | +3.10% | +3.08% |
| KORU/USDT:USDT | below_1h_threshold | +2.56% | +2.55% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.88% | +1.86% |
| MUU/USDT:USDT | below_1h_threshold | +1.70% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
