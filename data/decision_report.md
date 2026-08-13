# Decision Report

- generated_at: 2026-08-13T12:31:25.917401+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11443**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=11443, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.08% | **+1.98%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.23% | **+1.56%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.84% | **+1.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.67% | **+1.33%** |
| LIMIT_BB3S | 3/13 | 23.1% | +4.91% | **+1.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.40%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.47% | **+0.31%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$610.03** / 初期 $100.00 (+510.03%)
- 確定: 3961件 (Win 1237 / Loss 1296 / Flat 1428) / skip 4043件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $610.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.52** / 初期 $100.00 (+49.52%)
- 確定: 1631件 (Win 465 / Loss 389 / Flat 777) / skip 3223件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1291 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.99** / 初期 $100.00 (+15.99%)
- 確定: 1450件 (Win 426 / Loss 546 / Flat 478) / pending 3件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.99

## 6. Latest Market Context

- 更新: 2026-08-13T12:31:16.352519+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63527.0
- Funnel: target 978 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACU/USDT:USDT | +22.96% | $6,975,900.47 |
| AKE/USDT:USDT | +20.92% | $14,886,333.36 |
| COTI/USDT:USDT | +20.49% | $11,015,988.00 |
| BTW/USDT:USDT | +19.58% | $24,866,206.47 |
| AVAAI/USDT:USDT | +19.54% | $1,781,726.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAAI/USDT:USDT | below_1h_threshold | +3.58% | +3.47% |
| TST/USDT:USDT | below_1h_threshold | +2.16% | +2.05% |
| RE/USDT:USDT | below_1h_threshold | +1.84% | +1.74% |
| ALGO/USDT:USDT | below_1h_threshold | +1.51% | +1.40% |
| ONE/USDT:USDT | below_1h_threshold | +1.40% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
