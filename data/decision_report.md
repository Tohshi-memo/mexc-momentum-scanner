# Decision Report

- generated_at: 2026-08-13T14:16:42.075994+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11444**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=11444, expectancy=-0.01%
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
| LIMIT_ATR | 14/20 | 70.0% | +2.17% | **+1.52%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.84% | **+1.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.67% | **+1.33%** |
| LIMIT_BB3S | 3/13 | 23.1% | +4.91% | **+1.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.40%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.09% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$610.03** / 初期 $100.00 (+510.03%)
- 確定: 3962件 (Win 1237 / Loss 1296 / Flat 1429) / skip 4043件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $610.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.16** / 初期 $100.00 (+50.16%)
- 確定: 1632件 (Win 466 / Loss 389 / Flat 777) / skip 3223件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1304 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $150.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.99** / 初期 $100.00 (+15.99%)
- 確定: 1451件 (Win 426 / Loss 546 / Flat 479) / pending 5件 / skip 1464件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.99

## 6. Latest Market Context

- 更新: 2026-08-13T14:16:31.197204+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=63853.1
- Funnel: target 978 → liquid 176 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1, 4h RSI 79.9 >= 65=1, 4h RSI 81.6 >= 65=1, 4h RSI 71.9 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +46.30% | $21,649,566.67 |
| ACU/USDT:USDT | +32.35% | $7,552,388.69 |
| AVAAI/USDT:USDT | +21.30% | $1,855,237.34 |
| COTI/USDT:USDT | +21.14% | $11,362,045.22 |
| AVNT/USDT:USDT | +20.98% | $1,890,740.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_relative_strength | +5.10% | +4.86% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.95% | +4.71% |
| MYX/USDT:USDT | below_1h_threshold | +4.89% | +4.65% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.69% | +4.45% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.58% | +4.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
