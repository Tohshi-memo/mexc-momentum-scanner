# Decision Report

- generated_at: 2026-07-15T16:36:14.836113+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8756**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.90% / filled 20/20。**
- 全期間 MARKET基準: n=8756, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.78% | **+1.52%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.27% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.45% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.23% | **+0.13%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.18% | **+0.10%** |
| MARKET_LONG | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$341.20** / 初期 $100.00 (+241.20%)
- 確定: 2882件 (Win 902 / Loss 937 / Flat 1043) / skip 2435件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $341.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.77** / 初期 $100.00 (+5.77%)
- 確定: 720件 (Win 167 / Loss 167 / Flat 386) / skip 1447件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1160 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.58** / 初期 $100.00 (-1.42%)
- 確定: 63件 (Win 19 / Loss 40 / Flat 4) / pending 1件 / skip 164件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $98.58

## 6. Latest Market Context

- 更新: 2026-07-15T16:36:08.397224+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.77% price=64888.5
- Funnel: target 871 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +2.48% | $20,998,968.94 |
| KAITO/USDT:USDT | +1.76% | $2,722,648.48 |
| US/USDT:USDT | +0.87% | $7,783,746.44 |
| AAPLSTOCK/USDT:USDT | +0.50% | $1,608,735.37 |
| USOIL/USDT:USDT | +0.47% | $116,383,201.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.90% | +3.67% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.83% | +2.60% |
| KAITO/USDT:USDT | below_1h_threshold | +1.76% | +2.53% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +1.35% | +2.12% |
| US/USDT:USDT | below_1h_threshold | +0.80% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
