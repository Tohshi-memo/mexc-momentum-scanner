# Decision Report

- generated_at: 2026-09-06T12:31:22.187275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13811**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=13811, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.72% | **+0.58%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.72% | **+0.43%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.56% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.61% | **+1.45%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.57% | **+0.37%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.46% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$856.16** / 初期 $100.00 (+756.16%)
- 確定: 5117件 (Win 1537 / Loss 1674 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $856.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$193.21** / 初期 $100.00 (+93.21%)
- 確定: 2556件 (Win 716 / Loss 609 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $193.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.69** / 初期 $100.00 (+19.69%)
- 確定: 2423件 (Win 722 / Loss 923 / Flat 778) / pending 5件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $119.69

## 6. Latest Market Context

- 更新: 2026-09-06T12:31:10.395846+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=79936.1
- Funnel: target 1054 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +47.63% | $4,586,379.30 |
| ARB/USDT:USDT | +44.69% | $171,871,728.60 |
| FONE/USDT:USDT | +35.57% | $1,026,934.55 |
| FLOCK/USDT:USDT | +34.86% | $2,077,508.30 |
| SUSHI/USDT:USDT | +18.31% | $4,962,901.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LDO/USDT:USDT | below_1h_threshold | +2.07% | +2.00% |
| BASECAT/USDT:USDT | below_1h_threshold | +1.67% | +1.59% |
| WLD/USDT:USDT | below_1h_threshold | +1.22% | +1.15% |
| HYPE/USDT:USDT | below_1h_threshold | +1.22% | +1.15% |
| TAO/USDT:USDT | below_1h_threshold | +1.10% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
