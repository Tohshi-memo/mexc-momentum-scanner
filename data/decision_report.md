# Decision Report

- generated_at: 2026-08-21T03:46:46.469953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12141**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12141, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.16% | **+0.66%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.12% | **+0.64%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.93% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.36% | **+2.01%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.11% | **+1.71%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.59% | **+1.61%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.59% | **+1.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$653.72** / 初期 $100.00 (+553.72%)
- 確定: 4352件 (Win 1337 / Loss 1429 / Flat 1586) / skip 4350件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $653.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3730件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0573 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.21** / 初期 $100.00 (+17.21%)
- 確定: 1822件 (Win 540 / Loss 691 / Flat 591) / pending 2件 / skip 1792件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.21

## 6. Latest Market Context

- 更新: 2026-08-21T03:46:28.022822+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=74681.9
- Funnel: target 1011 → liquid 195 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.0 >= 65=1, 4h RSI 88.9 >= 65=1, 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +118.41% | $4,822,136.55 |
| ONG/USDT:USDT | +86.27% | $34,004,070.78 |
| BTW/USDT:USDT | +23.91% | $89,094,198.81 |
| ONT/USDT:USDT | +23.09% | $3,704,898.06 |
| ENA/USDT:USDT | +22.80% | $56,165,523.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +4.89% | +4.52% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.19% | +2.82% |
| GRASS/USDT:USDT | below_1h_threshold | +2.58% | +2.21% |
| CHIP/USDT:USDT | below_1h_threshold | +2.38% | +2.01% |
| KORU/USDT:USDT | below_1h_threshold | +2.02% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
