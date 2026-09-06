# Decision Report

- generated_at: 2026-09-06T12:46:21.604474+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13815**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=13815, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.27% | **+0.83%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.74% | **+0.37%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.43% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.23% | **+3.92%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.93% | **+0.74%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.57% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$847.62** / 初期 $100.00 (+747.62%)
- 確定: 5121件 (Win 1537 / Loss 1676 / Flat 1908) / skip 5255件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $847.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.86** / 初期 $100.00 (+91.86%)
- 確定: 2560件 (Win 716 / Loss 611 / Flat 1233) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0656 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $191.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.48** / 初期 $100.00 (+19.48%)
- 確定: 2426件 (Win 722 / Loss 924 / Flat 780) / pending 4件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.48

## 6. Latest Market Context

- 更新: 2026-09-06T12:46:11.544784+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79914.1
- Funnel: target 1054 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +60.18% | $5,655,695.22 |
| ARB/USDT:USDT | +43.87% | $175,175,839.81 |
| FONE/USDT:USDT | +35.23% | $1,043,029.64 |
| FLOCK/USDT:USDT | +29.50% | $2,187,741.92 |
| COTI/USDT:USDT | +20.12% | $1,366,995.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +2.14% | +2.10% |
| LDO/USDT:USDT | below_1h_threshold | +1.83% | +1.78% |
| COTI/USDT:USDT | below_1h_threshold | +1.46% | +1.42% |
| JTO/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| ZRO/USDT:USDT | below_1h_threshold | +0.93% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
