# Decision Report

- generated_at: 2026-08-13T10:31:24.192771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11436**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=11436, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.56% | **+1.48%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.44% | **+0.86%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.04% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.72% | **+1.55%** |
| LIMIT_FIB1272_LONG | 16/20 | 80.0% | +1.78% | **+1.42%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.41% | **+1.34%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.48% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$618.48** / 初期 $100.00 (+518.48%)
- 確定: 3954件 (Win 1236 / Loss 1292 / Flat 1426) / skip 4043件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.64% 残高後 $618.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.34** / 初期 $100.00 (+50.34%)
- 確定: 1624件 (Win 463 / Loss 385 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1322 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $150.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 1443件 (Win 425 / Loss 542 / Flat 476) / pending 4件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000227 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.27% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-08-13T10:31:15.259856+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=63584.6
- Funnel: target 973 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1, 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVAAI/USDT:USDT | +34.96% | $1,163,662.68 |
| AKE/USDT:USDT | +23.16% | $3,543,290.39 |
| ACU/USDT:USDT | +20.28% | $6,513,326.27 |
| BTW/USDT:USDT | +18.58% | $26,273,390.39 |
| COTI/USDT:USDT | +14.94% | $10,239,077.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +3.01% | +3.29% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.84% | +3.11% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.47% | +2.74% |
| VELVET/USDT:USDT | below_1h_threshold | +1.85% | +2.12% |
| ACU/USDT:USDT | below_1h_threshold | +1.66% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
