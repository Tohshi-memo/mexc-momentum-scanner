# Decision Report

- generated_at: 2026-07-16T06:41:12.672436+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8791**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.33% / filled 20/20。**
- 全期間 MARKET基準: n=8791, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.03% | **+1.83%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.04% | **+1.63%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.11% | **+1.48%** |
| LIMIT_BB3S | 5/11 | 45.5% | +2.64% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.07% | **+0.62%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +0.64% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.11% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$107.41** / 初期 $100.00 (+7.41%)
- 確定トレード: 103件 (TP 38 / SL 63 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$335.57** / 初期 $100.00 (+235.57%)
- 確定: 2906件 (Win 906 / Loss 945 / Flat 1055) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $335.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 754件 (Win 171 / Loss 169 / Flat 414) / skip 1448件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0316 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定: 65件 (Win 20 / Loss 41 / Flat 4) / pending 0件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000641 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $98.82

## 6. Latest Market Context

- 更新: 2026-07-16T06:41:06.309948+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=64656.2
- Funnel: target 874 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +27.22% | $13,484,275.69 |
| CAP/USDT:USDT | +18.09% | $2,628,051.44 |
| AKE/USDT:USDT | +12.31% | $50,084,135.96 |
| ROAM/USDT:USDT | +11.99% | $5,762,348.94 |
| LDO/USDT:USDT | +11.52% | $9,291,783.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.92% | +4.30% |
| MYX/USDT:USDT | below_1h_threshold | +3.36% | +3.73% |
| AKE/USDT:USDT | below_1h_threshold | +2.69% | +3.07% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.24% | +2.61% |
| SNXX/USDT:USDT | below_1h_threshold | +2.12% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
